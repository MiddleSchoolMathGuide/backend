FRONTEND := ./frontend
BACKEND := ./src

BUILD_CMD := npm run build

# Define targets
.PHONY: all build run

all: build run

build:
	@echo "Building frontend..."
	@cd $(FRONTEND) && $(BUILD_CMD)

run:
	@echo "Running backend..."
	@cd $(BACKEND) && py main.py
