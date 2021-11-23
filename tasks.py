from invoke import task

@task
def start(ctx):
    ctx.run("python3 src/jaturing.py")

@task
def test(ctx):
    ctx.run("pytest src")
