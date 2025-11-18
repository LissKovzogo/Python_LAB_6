#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def log_event(event_type, *messages, **options):

    level = options.get("level", "INFO")
    source = options.get("source", "SYSTEM")

    message = " ".join(str(msg) for msg in messages)

    print(f"[{level}] ({source}) – {message}")

if __name__ == '__main__':

    log_event("start", "Initialization complete", level="DEBUG", source="Core")
    log_event("shutdown", "System shutting down", level="WARNING")
    log_event("test", "Message 1", "Message 2", "Message 3", level = "key", source = "value")