#!/bin/bash
docker run -it --rm \
	--name nginxsso \
	-p 9080:80 \
	-v $(pwd)/nginx.conf:/etc/nginx/nginx.conf \
	-v $(pwd)/conf.d:/etc/nginx/conf.d \
	nginx:latest
