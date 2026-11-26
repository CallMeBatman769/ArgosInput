# ArgosInput

**ArgosInput** is a proof-of-concept (PoC) Python program that identifies users by their unique mouse-movement patterns. It explores behavioral biometrics by measuring cursor velocity over timed sessions to determine whether two separate sessions belong to the same person.

---

## How It Works

1. **Baseline Recording (Session 1):** After a 5-second countdown, ArgosInput records cursor coordinates and timestamps across multiple intervals (`NEEDED_TESTS`) for a set duration (`TEST_TIME`). It calculates the Euclidean distance between consecutive points to determine instantaneous speed in pixels per second, then computes an overall baseline average.
2. **Comparison Recording (Session 2):** After a second 5-second countdown, the program repeats the recording process to capture a comparison average.
3. **Evaluation:** ArgosInput calculates the percentage difference between the two average speeds:
   $$\text{Difference (\%)} = \frac{|\text{Average}_1 - \text{Average}_2|}{\text{Average}_1} \times 100$$
   - If the difference is **$\le 5\%$**, it outputs: `Likely same person`
   - If the difference is **$> 5\%$**, it outputs: `Different person`

---

## Prerequisites & Installation

ArgosInput relies on Python's built-in `time` and `math` modules, along with `pynput` for capturing global mouse events.

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/ArgosInput.git
   cd ArgosInput
   ```

2. **Install dependencies:**
   ```bash
   pip install pynput
   ```

---

## Usage

Run the script from your terminal:

```bash
python ArgosIn.py
```


Move your mouse naturally during both recording phases and follow the console prompts. (In the games folder there is a little mini game you can play for it!)

---

## Configuration

You can adjust the recording parameters at the top of the script to tweak sensitivity and test duration:

| Variable | Default | Description |
| :--- | :--- | :--- |
| `NEEDED_TESTS` | `2` | Number of consecutive recording intervals per session. |
| `TEST_TIME` | `20` | Duration (in seconds) of each individual recording interval. |
| `COUNTDOWN` | `["5", "4", "3", "2", "1"]` | Pre-recording countdown sequence in seconds. |

---

## Limitations & Future Improvements

As a proof of concept, ArgosInput currently relies solely on average cursor speed. Future iterations could expand accuracy by incorporating:
- **Acceleration & Jerk:** Measuring changes in speed rather than just mean velocity.
- **Trajectory & Curvature:** Analyzing path straightness, overshoot, and micro-corrections.
- **Click Dynamics:** Tracking click duration and double-click intervals.

---

## License

This project is open-source and available under the [MIT License](LICENSE).