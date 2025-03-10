# Kivy Android App

This is a basic Kivy application for Android.

## Setup

1. Create a virtual environment:
    ```sh
    python -m venv venv
    ```

2. Activate the virtual environment:
    - On Windows:
        ```sh
        .\venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```sh
        source venv/bin/activate
        ```

3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Run the application:
    ```sh
    python -m kivymd.tools.hotreload.main main.py --reload
    ```
