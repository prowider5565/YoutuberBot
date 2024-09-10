from fastapi.routing import APIRouter


router = APIRouter(prefix="/api")


@router.post("/download")
async def download_video_handler(request):
    pass




