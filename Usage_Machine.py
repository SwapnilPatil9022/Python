import tkinter as tk
import psutil

def get_application_usage():
    # Get a list of running processes
    running_processes = psutil.process_iter()
    
    # Clear the listbox
    app_usage_list.delete(0, tk.END)
    
    # Iterate through each process and retrieve usage information
    for proc in running_processes:
        try:
            # Retrieve process name and memory usage
            proc_name = proc.name()
            mem_usage = proc.memory_info().rss / (1024 * 1024)  # Memory usage in MB
            # Display process name and memory usage in the listbox
            app_usage_list.insert(tk.END, f"{proc_name}: {mem_usage:.2f} MB")
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

# Create a Tkinter window
root = tk.Tk()
root.title("Application Usage Display")

# Create a listbox to display application usage
app_usage_list = tk.Listbox(root, font=("Arial", 12), width=50)
app_usage_list.pack(pady=20)

# Button to fetch application usage
usage_button = tk.Button(root, text="Fetch Application Usage", command=get_application_usage)
usage_button.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
