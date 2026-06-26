import os

def save_pdf(uploaded_file):

    os.makedirs(
        "uploads",
        exist_ok=True
    )

    file_path = os.path.join(
        "uploads",
        uploaded_file.name
    )

    with open(
        file_path,
        "wb"
    ) as f:

        f.write(
            uploaded_file.getbuffer()
        )

    return file_path