# Dnssec-client

Small DNS client that resolves DNSSEC entries and make a http request to the given
domain.

Example usage:
```
docker run --rm -ti --dns=172.17.0.3  eloycoto/dnssec-client www.google.es
```
