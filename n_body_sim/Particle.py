from math import sqrt,tan
G = 6.67428*10**(-11) # Universal Gravitational constant -11 is og

class Particle():
    
    def __init__(self,pos,vel,mass=25):
        
        self.x = pos[0]
        self.y = pos[1]
        self.x_prev = []
        self.y_prev = []
        self.vx = vel[0]
        self.vy = vel[1]
        #self.ax = 0
        #self.ay = 0
        self.size = mass
        self.mass = mass*10**(24) # mass of earth ~ 10**24
        self.v_mag = 0
        
        #self.make_particle(self.x,self.y,mass)
        #self.update_pose()
        
        
    def draw_particle(self):
        '''draw the particle '''
        ellipse(self.x,self.y,self.size,self.size)
        
    def update_pose(self,accel=[0,0]):
        '''update position of the particle'''
        #dt = 1/frameRate
        dt = 0.001
   
        #print(accel)
        # boundary check
        if abs(self.x) >= 0.47*abs(width):
            accel[0] = -accel[0]*0.5
            self.vx = -self.vx
        if abs(self.y) >= 0.47*abs(height):
            accel[1] = -accel[1]*0.5
            self.vy = -self.vy
            
        self.x_prev.append(self.x)
        self.y_prev.append(self.y)
        
        if len(self.x_prev) == 500:
            self.x_prev = self.x_prev[250:500]
            self.y_prev = self.y_prev[250:500]
        
        self.x = self.x + dt*self.vx
        self.y = self.y + dt*self.vy
        self.vx = self.vx + dt*accel[0] 
        self.vy = self.vy + dt*accel[1]
        
        self.v_mag = sqrt(self.vx**2 + self.vy**2)
        
        
        
        
def rk4():
    
    k1 = h * dydx(x0, y) 
    k2 = h * dydx(x0 + 0.5 * h, y + 0.5 * k1) 
    k3 = h * dydx(x0 + 0.5 * h, y + 0.5 * k2) 
    k4 = h * dydx(x0 + h, y + k3) 

    # Update next value of y 
    y = y + (1.0 / 6.0)*(k1 + 2 * k2 + 2 * k3 + k4)
        
        
def attractionForce(p1,particles):
    '''calculates the gravitational force acting on a particle
    due to other particles utilizing the universal gravitatinoal const
    '''
    
    # find vector from particle to all particles
    vector = [[p2.x-p1.x,p2.y-p1.y] for p2 in particles ]
    vector.remove([0.0,0.0])
    magnitude = [sqrt(vec[0]**2 + vec[1]**2) for vec in vector]
    # check to make sure particle compare against itself/particle on top
    # of itself
    magnitude = [x if x != 0 else 1 for x in magnitude]


    # draw vectors
    draw_vectors = False
    if draw_vectors:
        for item in vector:
            x1 = p1.x
            y1 = p1.y
            x2 = x1 + item[0]
            y2 = y1 + item[1]
            
            line(x1,y1,x2,y2)
     
    #
    F = []
    
    for i,x in enumerate(vector):
        unit_vector = [x[0]/magnitude[i],x[1]/magnitude[i]]
        f = G*(p1.mass*particles[i].mass)/((magnitude[i]**2)*10**(8))
        F.append( [ unit_vector[0]*f, unit_vector[1]*f ] )

    

    return F


    
    
def accel_from_force(p1,particles):
    ''' calculate acceleration from 
    attraction force
    should return [x,y]
    ''' 
    # attraction force between masses
    F = attractionForce(p1,particles)
    np = len(particles)


    accel = [[f[0]/p1.mass,f[1]/p1.mass] for f in F ]
    #print(accel)
    #update_accel = [sum(accel[:][0])/np,sum(accel[:][1])/np] # average force
    if len(accel) == 1:
        update_accel = accel[0]
        
       
    else:
        #print('accel',accel)
        #print('accel :', accel[:][0])
        x = [item[0] for item in accel]
        y = [item[1] for item in accel]
        x = sum(x)
        y = sum(y)
    
        update_accel = [x,y] # summ of all forces
   
    #change colors with dramatic accel
    m_o_a = sqrt(update_accel[0]**2 + update_accel[1]**2) 
    #fill(m_o_a%255,255,255)
   
    fill(204,255,255)

    return update_accel
    


        
def particleMaker(number=1, pos=None,vel=None,sz=None):
    '''draws and positions particles in random location'''
    '''TODO: add variable for random values and seed'''
    pos_flag = 0
    vel_flag = 0
    sz_flag = 0
    
    if pos is None:
        pos_flag = 1
    if vel is None:
        vel_flag = 1
    if sz is None:
        sz_flag = 1
    particles = []
    
    for _ in range(number):
        
        if pos_flag: 
            pos = [random(-350,350),random(-350,350)]
        if vel_flag:
            vel = [random(-100.0,100.0),random(-400.0,400.0)]
        if sz_flag:
            sz = random(20,50)
    
        
        particles.append(Particle(pos,vel,sz))
        
    if number == 1:
        return Particle(pos,vel,sz)
    else:
        return particles
