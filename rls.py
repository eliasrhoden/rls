
class RLS:
    def __init__(self, theta0, P0 = None, lamb = 1):
        
        self.lamb = lamb
        
        self.N = len(theta0) 
        
        if type(theta0) != type(None):
            self.theta = theta0
        else:
            self.theta = np.zeros(th_dim)
            
        if type(P0) != type(None):
            self.P = P0
        else:
            self.P = np.eye(self.N)*1000
                

    def sample(self, phi, y):

        lamb = self.lamb
        
        P = self.P
        theta = self.theta
        
        K = P @ phi * 1/(lamb + phi.T @ P @ phi)
        P = (np.eye(self.N) - np.outer(K, phi))@P*1/lamb 

        theta = theta + K*(y - phi.T @ theta)
        
        self.theta = theta
        self.P = P
        
        return theta
    
    def get_estimate(self):
        return self.theta
    
    def get_variance(self):
        return self.P