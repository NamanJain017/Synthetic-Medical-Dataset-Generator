import typer
from src.routing.modality_router import ModalityRouter

app = typer.Typer(help="Synthetic Medical Imaging Dataset Generator CLI")

@app.command()
def generate(
    modality: str = typer.Option(..., help="Target modality (e.g., xray, ct)"),
    anatomy: str = typer.Option(..., help="Anatomical region"),
    disease: str = typer.Option(..., help="Pathology to inject"),
    severity: str = typer.Option("moderate", help="Severity level"),
    count: int = typer.Option(10, help="Number of images to generate"),
    output: str = typer.Option("./dataset", help="Output directory")
):
    """
    Generate synthetic medical datasets from the command line.
    """
    typer.echo(f"Initializing {modality} pipeline for {disease} in {anatomy}...")
    router = ModalityRouter()
    
    try:
        pipeline = router.get_pipeline(modality)
        typer.echo("Pipeline loaded successfully.")
        
        for i in range(count):
            typer.echo(f"Generating image {i+1}/{count}...")
            img = pipeline.generate(anatomy=anatomy, disease=disease, severity=severity)
            
        typer.echo(f"Generation complete. Saved to {output}")
        
    except Exception as e:
        typer.echo(f"Error during generation: {e}", err=True)

if __name__ == "__main__":
    app()
