from controller.main_controller import MainController

def main():
    # Create an instance of MainController to initialize the application
    controller = MainController()

    # Start the Tkinter event loop
    controller.view.mainloop()

if __name__ == "__main__":
    main()
