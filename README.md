# throughput_measurement_tools
Use server and client to measure processing speed.


## usage
### server start
```bash
APP_SERVER_PORT=8000 APP_COUNT_MAX=1000 ./server.py
```

### client start
```bash
APP_URL=http://localhost:8000 ./client.py
```

### use docker
```bash
docker pull mochi256/throughput_measurement_tools:latest
docker run -it throughput_measurement_tool /bin/bash
```
