"""
Docstring for physics.newton
"""

from dataclasses import dataclass
import math

@dataclass
class PhysicsResultDTO:
    total_time: float = 0.0
    max_height: float = 0.0
    distance_x: float = 0.0
    initial_velocity_y: float = 0.0
    final_velocity_y: float = 0.0
    velocity_x: float = 0.0

class KinematicsEngine:
    @staticmethod
    def mru(v: float, t: float):
        return v*t
    
    @staticmethod
    def get_vertical_data(v0: float, h:float=0, g:float=9.81):
        # If velocity is positive it going up, then gravity is negative
        if v0 > 0:
            t1 = v0/g
            y_max = h + v0*t1 - 0.5*g*(t1**2)
            
        # final_velocity and t from height to the ground
        vf = (v0**2 + 2*g*h)**(1/2)
        t2 = (vf - v0)/g

        # total_time equals 2 times the time from the positive v0 to the maximum heigth
        # plus the time from h to the ground
        total_time = t1*2 + t2 if t1 else t2
        max_height = y_max if y_max else h

        return PhysicsResultDTO(total_time=total_time, max_height=max_height, initial_velocity_y=v0, final_velocity_y=vf)
    
    @staticmethod
    def get_parabolic_data(v0:float, angulo_grados:float, h:float=0.0, g:float=9.81):
        # convert to radianes (Python uses radianes in math.sin/cos)
        theta = math.radians(angulo_grados)
        
        # get v0x and v0y
        v0x = v0 * math.cos(theta)
        v0y = v0 * math.sin(theta)
        
        # Reuse_get_vertical_data for y axis
        result = KinematicsEngine.get_vertical_data(v0y, h, g)
        
        # get horizontal distance
        distance_x = v0x * result.total_time

        result.distance_x = distance_x
        result.velocity_x = v0x
        
        return result