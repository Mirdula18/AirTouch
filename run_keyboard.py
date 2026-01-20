from virtual_keyboard import VirtualKeyboard
import sys

def main():
    print(" Virtual Keyboard with Hand Gesture Control")
    print("=" * 50)
    print(" Instructions:")
    print("   • Hold your hand in front of the camera")
    print("   • Move your index finger over keys to hover")
    print("   • Make a quick tap gesture to press keys")
    print("   • Press 'q' to quit the application")
    print("=" * 50)
    
    try:
        keyboard = VirtualKeyboard()
        keyboard.run()
    except KeyboardInterrupt:
        print("\n Application stopped by user")
    except Exception as e:
        print(f" Error: {e}")
        print(" Make sure you have a webcam connected and the required packages installed")
        print(" Install requirements: pip install -r requirements.txt")
        sys.exit(1)

if __name__ == "__main__":
    main()
