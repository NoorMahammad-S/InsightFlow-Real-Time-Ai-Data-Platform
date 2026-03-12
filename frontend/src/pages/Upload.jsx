import React from "react";

import Navbar from "../components/Navbar";
import FileUploader from "../components/FileUploader";

const Upload = () => {

  return (

    <div>

      <Navbar />

      <div style={{ padding: "20px" }}>

        <h2>Upload Dataset</h2>

        <p>
          Upload CSV or Excel datasets to ingest them into the InsightFlow
          analytics platform.
        </p>

        <FileUploader />

      </div>

    </div>

  );

};

export default Upload;