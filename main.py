from fastapi import APIRouter, FastAPI, HTTPException, Query
from kinematic import KinematicsEngine, PhysicsResultDTO

# Creamos la instancia de la aplicación
app = FastAPI(
    title="Physics Kinematics API",
    description="Physics API(Begining with kinematic)",
    version="1.0.0"
)

kinematics_router = APIRouter(prefix="/kinematics", tags=["Kinematics"])

# Endpoint para Lanzamiento Parabólico
@kinematics_router.get("/parabolic", response_model=PhysicsResultDTO)
def get_parabolic_calculation(
    v0: float,
    angle_deg: float,
    h: float = 0.0
):
    try:
        # Llamamos a tu motor que ya está testeado
        result = KinematicsEngine.get_parabolic_data(v0, angle_deg, h)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error en el cálculo: {str(e)}")

# Endpoint para Lanzamiento Vertical (caída libre o tiro hacia arriba)
@kinematics_router.get("/vertical", response_model=PhysicsResultDTO)
def get_vertical_calculation(v0: float, h: float = 0.0):
    return KinematicsEngine.get_vertical_data(v0, h)

app.include_router(kinematics_router)