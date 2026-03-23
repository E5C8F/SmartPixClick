# Smart PixClick

[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/E5C8F/SmartPixClick/pulls)

> [English](./README_English.md) | [中文](./README.md)

A desktop automation assistant based on visual recognition – record what you see, click where you recorded.

`Smart PixClick` is an innovative desktop automation tool. Instead of relying on traditional coordinate recording or element listening, it uses **window image & color recognition**. Through an intuitive process of "Record – Recognize – Click", it makes any repetitive on-screen task effortlessly automatable.

**Download:** [Smart PixClick.exe](https://github.com/E5C8F/SmartPixClick/blob/main/%E6%99%BA%E8%83%BD%E5%9B%BE%E8%89%B2%E7%82%B9%E5%87%BB%E5%99%A8.exe)
> **⚠️ Prototype Version Notice**: This release is a functional prototype focused on core technology validation. The user interface (UI) and some interactions are **not yet fully polished**. Please understand if you encounter any rough edges. Your feedback via Issues is greatly appreciated to help improve the project.
---

## ✨ Key Features

*   **🖱️ Intuitive Recording** – No coding required. Use simple hotkeys to capture the recognition area and target click position on the screen.
*   **🧠 Smart Recognition** – Combines **window title**, **area coordinates**, and **pixel data** for precise and reliable matching.
*   **⚙️ Flexible Execution** – Offers multiple recognition modes (from basic foreground click to forced window activation) to handle various scenarios.
*   **🎛️ Controllable Tolerance** – Customizable pixel color error tolerance effectively handles minor variations like screen flicker or font anti-aliasing.
*   **↩️ Reversible Operations** – Supports one-key undo for the last recorded script, making script management effortless.

---

## 🏆 Why Choose Smart PixClick?

Compared to other automation tools, Smart PixClick strikes the best balance between ease of use and practicality:

| Feature | **Smart PixClick** | **Key Press Wizard** | **AutoHotkey** | **Browser RPA** | **SikuliX** |
|:---|:---|:---|:---|:---|:---|
| **Core Tech** | **🔍 Window Image/Color** | 📍 Fixed Coordinates | 💻 Script/Image Hybrid | 🌐 DOM Analysis | 🖼️ Image Recognition |
| **Coding Required** | ✅ **None** | ⚠️ Partial | ❌ Must Program | ⚠️ Usually Not | ❌ Must Program |
| **Interaction Mode** | **🎯 State-Triggered**<br>Click when seen<br>Real-time recording & execution<br>Background window support | ⏱️ Sequential | 🔄 Flexible & Programmable | ⏱️ Sequential | 🔄 Visual Programming |
| **Ease of Use** | **⭐ Extremely Low**<br>Get started in 1 minute | ⭐⭐ Low | ⭐⭐⭐⭐ High | ⭐⭐ Low | ⭐⭐⭐ Moderate |
| **Dependencies** | **📦 None**<br>Ready to use | ⚠️ Some require install | 📦 Requires install | 🌐 Browser only | ☕ Requires Java |
| **Adaptability** | **🌟🌟🌟 Very High**<br>Window movement no issue | 🌟 Very Low | 🌟🌟🌟🌟🌟 Extremely High | 🌟🌟 Moderate | 🌟🌟 Moderate |
| **Best For** | **Any software**<br>Game automation<br>System dialogs | Fixed windows<br>Simple game macros | Complex logic<br>System-level tasks | Web automation<br>Data scraping | Test automation<br>Research |

---

## 🚀 Quick Start

### Record Your First Script

1.  **Launch** – Start Smart PixClick. In the console, just press Enter to use default settings.
2.  **Hover** – Move your mouse over the screen element you want the tool to recognize.
3.  **Record**:
    *   **Press and hold** the `Record Key` (default: **Numpad 9**).
    *   The area under the mouse will be captured as the **"recognition zone"**. (*Tip:* To avoid the element highlighting due to mouse hover, move the cursor away slightly while holding the key).
    *   Move your mouse to the target position you want to click.
    *   **Release** the `Record Key`. This position will be saved as the **"click point"**.
4.  **Done** – A script entry will appear in the list. The tool will automatically click when the recognition conditions are met.

### If a Script is Wrong

*   Press the `Undo Key` (default: **Numpad 0**) to remove the most recently recorded script.

---

## ⚙️ Configuration

### Script Executor Recognition Level (0-3)

| Level | Mode | Description |
| :--- | :--- | :--- |
| **0** | **Foreground Only** | Recognizes and clicks only in the active window. Fastest, minimal interference. |
| **1** | **Foreground + Window Adjustment** | Same as Level 0, but attempts to adjust the window to its recorded size and state. |
| **2** | **Background + Window Adjustment** | Recognizes and clicks in background windows (may not work for some apps). Attempts to restore window size/state. |
| **3** | **Forced Foreground + Window Adjustment** | Activates the target window to the foreground for recognition and click. Maximum compatibility. |

### Pixel Color Tolerance (0-255)

A pixel is considered a match if the difference in RGB values between the recorded and current pixel is **less than or equal to** this value.
*   **Recommended Value:** `16`. This effectively handles most anti-aliasing and minor brightness changes, balancing accuracy and fault tolerance.
*   **Lower value** = Stricter matching.
*   **Higher value** = Looser matching.

---

## 💡 Use Cases

*   **🛠️ Software Testing** – Automate repetitive functional regression tests.
*   **🎮 Game Automation** – Automate daily tasks (please comply with the game's terms of service).
*   **💼 Office Automation** – Automate repetitive desktop tasks like report generation or data entry.
*   **♿ Accessibility** – Simplify complex operations for users with mobility challenges.

---

## ❓ FAQ

**Q: Why does recognition sometimes fail after recording?**
**A:** The most common reason is that the mouse hover caused the element to highlight or change color. After pressing the record key, **briefly move the mouse away** to capture the element in its default state.

**Q: Why doesn't background click (Level 2) work on some programs?**
**A:** This is expected. Background simulation relies on the system's message mechanism, which some applications (especially those with anti-cheat systems or high-privilege requirements) block.

**Q: What if the tool doesn't work on a window that requires administrator privileges?**
**A:** By default, the tool runs with normal privileges. To interact with elevated windows, please **run Smart PixClick as an administrator**.

**Q: Can I save my configuration and scripts?**
**A:** **The current version does not support persistent saving of configurations and scripts.** You will need to reconfigure and re-record scripts each time you launch the tool. As a workaround, all script data changes are printed in real-time to the console; advanced users can copy this data for manual backup. In developer mode (type `0` in the console), you can re-import saved script data (requires relevant knowledge; not recommended for general users).

**Q: I clicked a button in Window A that opened Window B, but the tool keeps clicking the button in Window A. Why?**
**A:** This occurs because the image/color of the button in Window A hasn't changed after being clicked. The tool still sees a valid trigger condition. This is an inherent characteristic of image/color-based automation. **Solution**: When recording such workflows, ensure the recorded visual element changes after the action, or use recognition level 0 or 1, which will not recognize windows that are covered.

**Q: Is the tool safe?**
**A:** Smart PixClick runs entirely locally and does not upload any screen data or images to the network. It performs no network activities, so it cannot perform update checks.

---

## 🤝 How to Contribute

We welcome all contributions! This includes:
*   🐛 Reporting bugs
*   💡 Suggesting new features
*   📝 Improving documentation
*   🔧 Submitting pull requests

Please visit our [Issue page](https://github.com/E5C8F/SmartPixClick/issues) to get involved.

---

**Turn repetitive clicks into history. Focus on what truly matters.**
