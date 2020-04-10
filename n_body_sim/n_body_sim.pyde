from Particle import Particle, particleMaker,accel_from_force
        
        
particles = particleMaker(number=4)
#giant = particleMaker(sz=300,vel=[5,0])
#particles.insert(-1,giant)
avg = 0

def setup():
    size(800,700)
    #frameRate(30)
    translate(width/2,height/2)
    #particles = particleMaker(10)
    #frameRate()
    

def draw():
    global particles,avg
    
    background(255,229,204)
    pushStyle()
    fill(0)
    text(frameRate,width/20,height/20)
    text('Average Velocity:',width/20,height/15)
    text(avg,(width/20)+(width/8),(height/15)+1)
    text('m/s',(width/20)+(width/4.8),(height/15)+1)
    popStyle()
    
    translate(width/2,height/2)
    ambientLight(102, 102, 102)
    #giant.draw_particle()
    #gacc = accel_from_force(giant,particles)
    #giant.update_pose(gacc)
    
    vel = 0
    for particle in particles:
        '''redraw particle and update position'''
        #print('pos',[particle.x,particle.y])
        #noSmooth()
        
        particle.draw_particle()
        accel = accel_from_force(particle,particles)
        particle.update_pose(accel)
        vel += particle.v_mag

        
        for i in range(len(particle.x_prev)):
            pushStyle()
            stroke(41,255,255)
            point(particle.x_prev[i],particle.y_prev[i])
            popStyle()
    
    avg = vel/len(particles)
            
    
   
    
        
    
        
        
        
    
        
        



    
        
        
        
          
