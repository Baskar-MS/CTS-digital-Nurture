# ==========================================
# Task 1: Request-Response Cycle in Django
# ==========================================

# 1. Request-Response Cycle
#
# Browser sends GET request to:
# /api/courses/
#
# Step 1:
# The request reaches Django through WSGI/ASGI.
#
# Step 2:
# Middleware processes the incoming request.
#
# Step 3:
# URL Router (urls.py) matches the requested URL.
#
# Step 4:
# The corresponding View function/class is executed.
#
# Step 5:
# If data is needed, the View communicates with the Model.
#
# Step 6:
# The Model interacts with the database and returns data.
#
# Step 7:
# The View prepares an HttpResponse or JSON response.
#
# Step 8:
# Middleware processes the outgoing response.
#
# Step 9:
# The response is sent back to the browser.


# ==========================================
# 2. Middleware
# ==========================================

# Middleware sits between the request and the view.
# It processes requests before they reach the view
# and processes responses before they reach the browser.

# Example Built-in Middleware:

# SecurityMiddleware
# Adds security-related HTTP headers and protects
# against common security attacks.

# SessionMiddleware
# Enables session support so users can stay logged in
# and maintain session data.


# ==========================================
# 3. WSGI vs ASGI
# ==========================================

# WSGI (Web Server Gateway Interface)
# - Handles synchronous requests.
# - Suitable for traditional web applications.
# - Django uses WSGI by default.

# ASGI (Asynchronous Server Gateway Interface)
# - Supports asynchronous programming.
# - Handles WebSockets, long-lived connections,
#   and real-time applications.
# - Switch to ASGI when building chat applications,
#   live notifications, or other async services.


# ==========================================
# 4. MVC vs MVT
# ==========================================

# MVC
# M - Model
# V - View
# C - Controller

# Django uses MVT

# Model    -> Model
# View     -> Template
# Controller -> Django View

# Therefore:
# MVC Model = Django Model
# MVC View = Django Template
# MVC Controller = Django View