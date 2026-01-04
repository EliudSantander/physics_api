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
    v0: float = Query(..., gt=0, description="Initial velocity (m/s)"),
    angle_deg: float = Query(..., ge=0, le=90, description="Angle in degrees (0-90)"),
    h: float = Query(0.0, ge=0)
):
    try:
        # Llamamos a tu motor que ya está testeado
        result = KinematicsEngine.get_parabolic_data(v0, angle_deg, h)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error en el cálculo: {str(e)}")

# Endpoint para Lanzamiento Vertical (caída libre o tiro hacia arriba)
@kinematics_router.get("/vertical", response_model=PhysicsResultDTO)
def get_vertical_calculation(
    v0: float = Query(..., description="Initial velocity (m/s). Positive for up, negative for down."),
    h: float = Query(0.0, ge=0, description="Initial height (m). Must be 0 or positive.")
):
    try:
        return KinematicsEngine.get_vertical_data(v0, h)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Physics Calculation Error: {str(e)}")

app.include_router(kinematics_router)