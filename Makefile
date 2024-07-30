# Paths
FRONTEND := ./frontend
BACKEND := ./src

# MongoDB
# Warning: Tool "mongosh" needed
MONGO_HOST := localhost
MONGO_PORT := 27017
MONGO_DB := MSMGWeb
PURGE_JS := tools/db/purge.js

BUILD_CMD := npm run build
INSTALL_FE_CMD := npm install
INSTALL_BE_CMD := pip install -r requirements.txt

# Define targets
.PHONY: all build run

all: build run

install:
	@echo "Installing required software(s)"
	@cd $(FRONTEND) && $(INSTALL_FE_CMD)
	$(INSTALL_BE_CMD)

build:
	@echo "Building frontend..."
	@cd $(FRONTEND) && $(BUILD_CMD)

run:
	@echo "Running backend..."
	@cd $(BACKEND) && py main.py

purge:
	@echo "Purging database $(MONGO_DB)..."
	@read -p "Are you sure you want to purge database? [y/N] " confirm; \
	if [ "$$confirm" = "y" ]; then \
		mongosh --host $(MONGO_HOST) --port $(MONGO_PORT) $(MONGO_DB) $(PURGE_JS); \
		echo "Done."; \
	else \
		echo "Aborted"; \
	fi
