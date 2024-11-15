def install_whl():
    plugin_dir = os.path.dirname(__file__)
    whl_path = os.path.join(plugin_dir, 'earthengine_api-1.3.1-py3-none-any.whl')
    
    if os.path.exists(whl_path):
        try:
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', whl_path])
            print("Installation successful.")
        except subprocess.CalledProcessError as e:
            print(f"Installation failed: {e}")
    else:
        print("Wheel file not found in the plugin folder.")

try:
    import ee
    print("Earth Engine API is already installed.")
except ImportError:
    install_whl()
    import ee
