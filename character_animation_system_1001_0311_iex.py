# 代码生成时间: 2025-10-01 03:11:23
import tkinter as tk
from tkinter import Canvas, PhotoImage

# 角色动画类
class CharacterAnimation:
    def __init__(self, master, image_path, position, frame_count):
        self.master = master
        self.image_path = image_path
        self.position = position
        self.frame_count = frame_count
        self.current_frame = 0
        self.image_sequence = []
        self.load_images()

    def load_images(self):
        """加载所有帧的图像。"""
        try:
            for i in range(self.frame_count):
                image = PhotoImage(file=self.image_path.format(i))
                self.image_sequence.append(image)
        except Exception as e:
            print(f"Error loading images: {e}")

    def update_frame(self):
        """更新到下一帧图像。"""
        if self.current_frame < self.frame_count - 1:
            self.current_frame += 1
        else:
            self.current_frame = 0
        self.draw_frame()

    def draw_frame(self):
        """绘制当前帧的图像。"""
        if hasattr(self, 'canvas_item'):
            self.canvas.delete(self.canvas_item)
        self.canvas_item = self.canvas.create_image(self.position, image=self.image_sequence[self.current_frame])

# 动画系统主窗口类
class AnimationSystem:
    def __init__(self, root):
        self.root = root
        self.root.title('Character Animation System')
        self.canvas = Canvas(self.root, width=800, height=600)
        self.canvas.pack()
        self.character = CharacterAnimation(self.root, 'frame_{}.png', (400, 300), 10)
        self.running = False

    def start_animation(self):
        """开始动画。"""
        if not self.running:
            self.running = True
            self.animate()

    def stop_animation(self):
        """停止动画。"""
        self.running = False

    def animate(self):
        """动画的主循环。"""
        if self.running:
            self.character.update_frame()
            self.root.after(100, self.animate)

# 主函数
def main():
    root = tk.Tk()
    animation_system = AnimationSystem(root)
    root.protocol('WM_DELETE_WINDOW', lambda: animation_system.stop_animation())
    root.after(100, animation_system.start_animation)
    root.mainloop()

if __name__ == '__main__':
    main()