# Docker pipelines

Each V2 use case has its own small image. Docker Compose is not used; the daemon
is sufficient. Build and run from the repository root.

| Image | Command |
| --- | --- |
| `frontierforge:quantum` | `docker build -f docker/Dockerfile.quantum -t frontierforge:quantum . && docker run --rm frontierforge:quantum` |
| `frontierforge:neuro` | `docker build -f docker/Dockerfile.neuro -t frontierforge:neuro . && docker run --rm frontierforge:neuro` |
| `frontierforge:bayes` | `docker build -f docker/Dockerfile.bayes -t frontierforge:bayes . && docker run --rm frontierforge:bayes` |
| `frontierforge:photonic` | `docker build -f docker/Dockerfile.photonic -t frontierforge:photonic . && docker run --rm frontierforge:photonic` |
| `frontierforge:cellular` | `docker build -f docker/Dockerfile.cellular -t frontierforge:cellular . && docker run --rm frontierforge:cellular` |
| `frontierforge:reversible` | `docker build -f docker/Dockerfile.reversible -t frontierforge:reversible . && docker run --rm frontierforge:reversible` |
| `frontierforge:reservoir` | `docker build -f docker/Dockerfile.reservoir -t frontierforge:reservoir . && docker run --rm frontierforge:reservoir` |
| `frontierforge:tests` | `docker build -f docker/Dockerfile.tests -t frontierforge:tests . && docker run --rm frontierforge:tests` |

Run every image with `./docker/run_all.sh`. All images are based on
`python:3.12-slim`, install no third-party packages, and execute a fixed seeded
demo so output is reproducible. Full local and Docker logs are recorded in
`docs/TEST-RESULTS.md`.

Docker is a verification environment only; results remain CPU simulations and
are not evidence of quantum, photonic, or energy advantage.
