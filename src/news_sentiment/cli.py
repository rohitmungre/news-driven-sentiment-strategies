import typer
from .fetcher import fetch_headlines
from .analyzer import analyze

app = typer.Typer(help="Fetch news and run sentiment analysis")

@app.command()
def run(
    query: str = typer.Argument(..., help="Search term"),
    limit: int = typer.Option(10, "--limit", "-n", help="Number of articles"),
):
    """Fetch headlines for QUERY and analyze sentiment."""
    typer.echo(f"Fetching top {limit!r} articles on {query!r}…")
    texts = fetch_headlines(query, limit)
    results = analyze(texts)
    for art, res in zip(texts, results):
        typer.secho(f"\n» {res['label']} ({res['score']:.2f})", fg="cyan")
        typer.echo(art or "[no content]")
