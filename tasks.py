from invoke import task

@task
def start(xtc):
    ctx.run("python3 src/jaturing.py")
