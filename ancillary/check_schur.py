"""Finite indexing/convention controls, NOT a proof of the paper's theorems."""
import numpy as np

TOL = 2e-11
def close(a, b, label):
    error = np.linalg.norm(a-b)
    assert error < TOL, (label, error)
    print('PASS', label, 'residual', f'{error:.3g}')

omega = np.exp(2j*np.pi/3)
diagonals = np.array([[1,1/np.sqrt(3),1/np.sqrt(3),1/np.sqrt(3)],
                      [0,np.sqrt(2/3),np.sqrt(2/3)*omega,np.sqrt(2/3)*omega**2]])
K = [np.diag(row) for row in diagonals]
close(sum(x.conj().T@x for x in K), np.eye(4), 'trace preservation')
products = np.stack([(a.conj().T@b).diagonal() for a in K for b in K])
singular = np.linalg.svd(products, compute_uv=False)
assert singular[-1] > .5
print('PASS Kraus-product independence; minimum singular value', singular[-1])
vec = np.stack([a.reshape(-1) for a in K], axis=1)
choi = vec@vec.conj().T/4
close(np.linalg.eigvalsh(choi), np.array([0]*14+[.5,.5]), 'flat Choi spectrum')
q = diagonals.conj().T
Pi = [np.outer(x,x.conj()) for x in q]
close(sum(Pi), 2*np.eye(2), 'SIC tightness')
close(np.array([[np.trace(a@b) for b in Pi] for a in Pi]),
      (2*np.eye(4)+np.ones((4,4)))/3, 'SIC overlaps')

def theta(z): return np.diag([np.trace(z@p)/2 for p in Pi])
def inverse(x): return sum(x[i,i]*(3*Pi[i]-np.eye(2)) for i in range(4))
for a in range(2):
    for b in range(2):
        z = np.zeros((2,2),complex); z[a,b]=1
        close(inverse(theta(z)), z, f'inverse E{a}{b}')
        support = vec/np.sqrt(2)
        joint = (support@z@support.conj().T).reshape(4,4,4,4)
        close(np.einsum('iyjy->ij', joint), theta(z), f'partial-trace convention {a}{b}')

# Amplified inverse on a fixed arbitrary operator (three-dimensional spectator).
ref_rng=np.random.default_rng(20260916)
z=ref_rng.normal(size=(6,6))+1j*ref_rng.normal(size=(6,6))
blocks=z.reshape(2,3,2,3)
x=np.zeros((4,3,4,3),complex)
for i in range(4):
    x[i,:,i,:]=sum(Pi[i][b,a]*blocks[a,:,b,:]/2 for a in range(2) for b in range(2))
recovered=sum(np.kron(3*Pi[i]-np.eye(2),x[i,:,i,:]) for i in range(4))
close(recovered,z,'inverse with three-dimensional spectator')

# One completely fixed small realization. The proof's conservative dimensions
# are not used as a practical algorithm. This tests all index maps and polars.
rng = np.random.default_rng(20260915)
k, r, m = 2, 2, 128
G=(rng.normal(size=(k,m,r))+1j*rng.normal(size=(k,m,r)))/np.sqrt(2*m)
Gamma=G.transpose(2,1,0).reshape(r*m,k)/np.sqrt(r)
def polar(a):
    u,_,vh=np.linalg.svd(a,full_matrices=False)
    return u@vh
J=polar(Gamma)
close(J.conj().T@J,np.eye(k),'virtual polar isometry')
V=[]; W=[]; slice_defects=[]
for i in range(4):
    F=np.einsum('a,amr->mr',diagonals[:,i],G)
    wi=polar(F)
    close(wi.conj().T@wi,np.eye(r),'physical polar isometry '+str(i))
    close(Gamma@diagonals[:,i],F.T.reshape(-1)/np.sqrt(r),'vectorization '+str(i))
    V.append(wi.T.reshape(-1)/np.sqrt(r))
    W.append(J@diagonals[:,i])
    slice_defects.append(np.linalg.norm(F.conj().T@F-np.eye(r),2))
delta=max(slice_defects+[np.linalg.norm(Gamma.conj().T@Gamma-np.eye(k),2)])
assert delta < 1
error=max(np.linalg.norm(a-b) for a,b in zip(V,W))
assert error <= 2*delta + TOL
print('PASS common dilation comparison; defect',delta,'distance',error)
# Small arbitrary reference convention check (not a diamond optimization).
psi=rng.normal(size=(4,3))+1j*rng.normal(size=(4,3)); psi/=np.linalg.norm(psi)
actual=np.einsum('is,ie->ise',psi,np.stack(V)).reshape(12,r*m)
target=np.einsum('is,ie->ise',psi,np.stack(W)).reshape(12,r*m)
diff=actual@actual.conj().T-target@target.conj().T
half_trace=np.linalg.svd(diff,compute_uv=False).sum()/2
assert half_trace <= error+TOL
print('PASS reference-state control; half trace distance',half_trace)
print('All finite controls passed; no all-dimension, entropy, or priority certification.')
