# ClassMark 🎓

**AI-powered attendance system using face and voice recognition**

🚀 [Live App](https://classmark-main.streamlit.app/) · 🌐 [Project Website](https://cm-landing-page-iota.vercel.app/)

## 📖 About

ClassMark replaces manual roll-calls. A teacher uploads classroom photos or records a short audio clip, the app identifies enrolled students, and the teacher reviews and saves the attendance.

## ✨ Features

- 📸 **Face attendance:** detects faces in classroom photos and matches them to enrolled students
- 🎙️ **Voice attendance:** identifies students from a single classroom recording
- 🔐 **Face ID login** for students, password login for teachers (bcrypt-hashed)
- 📱 **QR / link enrollment:** students join a subject via code, link or QR
- ✅ **Review before saving:** teachers confirm results before they are stored
- 📊 **Records:** per-session summary for teachers (CSV download), per-subject counts for students

## ⚙️ How It Works

1. A student registers once; a 128-d face embedding (dlib) and an optional voice embedding (Resemblyzer) are stored in Supabase.
2. For face attendance, faces are detected in each photo, classified with an SVM, and accepted only if the distance to the stored embedding is within a threshold.
3. For voice attendance, the recording is split on silence, each segment is embedded, and matched to enrolled students by cosine similarity.
4. The teacher reviews the table and saves it to the `attendance_logs` table.

## 🛠️ Tech Stack

| Layer | Tools |
| --- | --- |
| App | Streamlit, Pandas, Segno (QR) |
| Face recognition | dlib, face_recognition_models, scikit-learn |
| Voice recognition | Resemblyzer, Librosa |
| Auth | bcrypt |
| Database | Supabase (PostgreSQL) |

## 🗄️ Database Tables

`teachers`, `students`, `subjects`, `subject_students`, `attendance_logs`

## 🚀 Run Locally

```bash
git clone https://github.com/AnishaSinha01/classmark
cd classmark
pip install -r requirements.txt
```

Create `.streamlit/secrets.toml`:

```toml
SUPABASE_URL = "your-project-url"
SUPABASE_KEY = "your-key"
```

```bash
streamlit run app.py
```

Python 3.12 recommended.

## ⚠️ Known Limitations

- Face login has no liveness check (a photo of a person could be accepted).
- Each student has one face embedding; accuracy depends on photo quality and face size.
- Students join a subject using its subject code, so two teachers using the same code can clash. A unique per-subject join code is the planned fix.

## 🔒 Privacy

Face and voice embeddings are used only for attendance. Never commit `secrets.toml`.
