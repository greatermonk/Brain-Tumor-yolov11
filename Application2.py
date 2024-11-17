import tkinter as tk
import ultralytics
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import os
from ultralytics import YOLO
from get_tumour_description import get_tumour_details


class BrainTumorDetector:
    def __init__ (self, root):
        self.root = root
        self.root.title("Brain Tumor Detection System")

        # Set minimum window size
        self.root.minsize(1000, 600)
        self.root.configure(bg="black")

        # Load YOLO model
        try:
            self.model = YOLO("last.pt")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load YOLO model:\n{str(e)}")
            root.destroy()
            return

        # Create main frame
        self.main_frame = tk.Frame(self.root, bg='#28282b')
        self.main_frame.pack(expand=True, fill='both', padx=20, pady=15)

        # Create button frame
        self.button_frame = tk.Frame(self.main_frame)
        self.button_frame.pack(pady=(0, 30))

        # Create Browse button
        self.browse_button = tk.Button(
            self.button_frame,
            text="Browse Image",
            command=self.browse_image,
            width=20,
            fg='black',
            height=2,
            border='4px dark blue',
            bg="#839496",
            takefocus=1,
            activebackground='#cae7d3',
            activeforeground='#253342'

        )
        self.browse_button.pack(side='left')

        # Create image frames
        self.image_container = tk.Frame(self.main_frame,  bg='light grey')
        self.image_container.pack(expand=True, fill='both')

        # Left frame for original image
        self.left_frame = tk.Frame(self.image_container,  bg='grey', borderwidth=4)
        self.left_frame.pack(side='left', expand=True, fill='both', padx=5, pady=5)

        # Right frame for detection result
        self.right_frame = tk.Frame(self.image_container,  bg='grey', borderwidth=4)
        self.right_frame.pack(side='left', expand=True, fill='both', padx=5, pady=5)

        # Labels for images
        self.original_label = tk.Label(
            self.left_frame,
            text="Original MRI Scan",
            font=('Courier', 16, 'bold'),
            relief='raised',
            border = '2px',
            bg = '#fffff0'
        )
        self.original_label.pack()

        self.detection_label = tk.Label(
            self.right_frame,
            text="Detected Tumour: ",
            font=('Courier', 16, 'bold'),
            relief='raised',
            border='2px',
            bg='#fffff0'

        )
        self.detection_label.pack()

        # Create image labels
        self.original_image_label = tk.Label(
            self.left_frame,
            text="No image selected",
            bg='#e7eae5',
            relief='sunken',
            font=('Consolas, monospace', 14, 'italic'),
            fg='light grey',
            highlightbackground='yellow'
        )
        self.original_image_label.pack(expand=True, fill='both')

        self.detected_image_label = tk.Label(
            self.right_frame,
            text="Detection result will appear here",
            bg='#e7eae5',
            relief='sunken',
            font = ('Consolas, monospace', 14, 'italic'),
            fg = 'light grey',
            highlightbackground = 'yellow',
            pady=10
        )
        self.detected_image_label.pack(expand=True, fill='both')

        # Create result text
        self.result_label = tk.Label(
            self.main_frame,
            text="Detection Result: None",
            font=('Roboto', 16),
            pady=10,
            padx=15,
            border = '5px dark orange',
            borderwidth = 5,
            bg='#586E75',
            fg='white',
            relief='raised'

        )
        self.result_label.pack(expand=True)

        self.details = tk.Label(
            self.main_frame,
            relief='groove',
            anchor="sw",
            text="Details About Tumour",
            pady=2,
            padx=4,
            font=('Georgia', 15),
            border = '4px black',
            bg = "#b3b3b3"
        )
        self.details.pack(fill="y", expand=False)

        # Store references
        self.current_image = None
        self.current_image_path = None
        self.original_image = None
        self.detection_image = None

    def browse_image (self):
        file_path = filedialog.askopenfilename(
            filetypes=[
                ("Image files", "*.png *.jpg *.jpeg"),
                ("All files", "*.*")
            ]
        )
        if file_path:
            self.current_image_path = file_path
            self.process_image()

    def process_image (self):
        if not self.current_image_path:
            return
        try:
            # Load and display original image
            self.original_image = Image.open(self.current_image_path)
            self.display_image(self.original_image, self.original_image_label)

            # Perform detection
            results = self.model.predict(self.current_image_path)
            detection_plot = results[0].plot(pil=True)
            self.detection_image = Image.fromarray(detection_plot)
            self.display_image(self.detection_image, self.detected_image_label)

            # Prepare detection text and tumor details
            detection_text = "Detection Result: "
            detected_items = []
            for detections in results:
                for objects in detections.boxes:
                    class_id = int(objects.cls)
                    class_name = self.model.names[class_id]
                    detected_items.append(class_name)

            # Update result and tumor details
            if detected_items:
                detection_text += ", ".join(detected_items)
                self.result_label.config(text=detection_text)

                # Get tumor details for the first detected item (assuming one tumor per image)
                predicted_class = detected_items[0]
                tumor_details = get_tumour_details(predicted_class)
                self.details.config(text=tumor_details)  # Update details label with tumor details
                self.root.title(f"Brain Tumor Detection - {os.path.basename(self.current_image_path)}")
            else:
                detection_text += "No tumor detected"
                self.result_label.config(text=detection_text)
                self.details.config(text="Details About Tumour: No tumor detected")

        except Exception as e:
            messagebox.showerror("Error", f"Failed to process image:\n{str(e)}")
            self.clear_display()

    def display_image (self, image, label):
        # Get label size
        label_width = label.winfo_width()
        label_height = label.winfo_height()

        # Ensure minimum dimensions
        label_width = max(label_width, 400)
        label_height = max(label_height, 400)

        # Resize image to fit label while maintaining aspect ratio
        display_size = self.get_display_size(image.size, (label_width, label_height))
        resized_image = image.resize(display_size, Image.Resampling.LANCZOS)

        # Convert to PhotoImage
        photo = ImageTk.PhotoImage(resized_image)

        # Update label
        label.config(image=photo, text="")
        label.image = photo  # Keep a reference

    def get_display_size (self, image_size, frame_size):
        # Calculate scaling factors
        width_ratio = frame_size[0] / image_size[0]
        height_ratio = frame_size[1] / image_size[1]
        scale_factor = min(width_ratio, height_ratio)

        # Calculate new dimensions
        new_width = int(image_size[0] * scale_factor)
        new_height = int(image_size[1] * scale_factor)

        return (new_width, new_height)

    def clear_display (self):
        self.current_image_path = None
        self.original_image = None
        self.detection_image = None
        self.original_image_label.config(image="", text="No image selected")
        self.detected_image_label.config(image="", text="Detection result will appear here")
        self.result_label.config(text="Detection Result: None")
        self.root.title("Brain Tumor Detection System")

    def on_resize (self, event):
        # Only resize if it's a window resize event
        if event.widget == self.root:
            # Add a small delay to prevent multiple resize events
            self.root.after_cancel(self._resize_job) if hasattr(self, '_resize_job') else None
            self._resize_job = self.root.after(250, self.resize_images)

    def resize_images (self):
        if self.original_image:
            self.display_image(self.original_image, self.original_image_label)
        if self.detection_image:
            self.display_image(self.detection_image, self.detected_image_label)


if __name__ == "__main__":
    root = tk.Tk()
    app = BrainTumorDetector(root)

    # Bind resize event
    root.bind('<Configure>', app.on_resize)

    root.mainloop()