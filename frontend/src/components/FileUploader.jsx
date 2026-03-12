import React, { useState } from "react";
import axios from "axios";

const FileUploader = () => {
  const [file, setFile] = useState(null);
  const [status, setStatus] = useState("");

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const uploadFile = async () => {
    if (!file) {
      setStatus("Please select a file.");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);

    try {
      await axios.post("http://localhost:8000/api/upload", formData, {
        headers: {
          "Content-Type": "multipart/form-data"
        }
      });

      setStatus("Upload successful.");
    } catch (error) {
      setStatus("Upload failed.");
    }
  };

  return (
    <div style={{ marginTop: "20px" }}>
      <h3>Upload Dataset</h3>

      <input type="file" onChange={handleFileChange} />

      <button onClick={uploadFile} style={{ marginLeft: "10px" }}>
        Upload
      </button>

      <p>{status}</p>
    </div>
  );
};

export default FileUploader;