# GUI Implementation
class DeadlockToolkitApp:
    def _init_(self, root):
        self.root = root
        self.root.title("Deadlock Prevention and Recovery Toolkit")

        # Input fields
        self.processes_label = tk.Label(root, text="Processes (comma-separated):")
        self.processes_label.grid(row=0, column=0)
        self.processes_entry = tk.Entry(root)
        self.processes_entry.grid(row=0, column=1)

        self.resources_label = tk.Label(root, text="Resources (comma-separated):")
        self.resources_label.grid(row=1, column=0)
        self.resources_entry = tk.Entry(root)
        self.resources_entry.grid(row=1, column=1)

        self.available_label = tk.Label(root, text="Available Resources (comma-separated):")
        self.available_label.grid(row=2, column=0)
        self.available_entry = tk.Entry(root)
        self.available_entry.grid(row=2, column=1)
