// src/components/ResumeUpload.jsx

import React, { useState } from "react";
import { Button, Typography, Box, CircularProgress, Paper } from "@mui/material";
import axios from "axios";

const ResumeUpload = () => {
  const [file, setFile] = useState(null);
  const [loading, setLoading] = useState(false);
  const [feedback, setFeedback] = useState("");

  const handleUpload = async () => {
    if (!file) return;
    setLoading(true);

    const formData = new FormData();
    formData.append("file", file);

    try {
      const res = await axios.post("http://localhost:8000/analyze-resume/", formData, {
        headers: { "Content-Type": "multipart/form-data" },
      });

      setFeedback(res.data.feedback);
    } catch (err) {
      setFeedback("Something went wrong.");
    }

    setLoading(false);
  };

  return (
    <Box display="flex" flexDirection="column" alignItems="center" mt={5} gap={2}>
      <Typography variant="h4">Upload Your Resume</Typography>
      <input
        type="file"
        accept=".pdf"
        onChange={(e) => setFile(e.target.files[0])}
        style={{ marginTop: "1rem" }}
      />
      <Button
        variant="contained"
        color="primary"
        onClick={handleUpload}
        disabled={loading || !file}
      >
        {loading ? "Analyzing..." : "Analyze Resume"}
      </Button>

      {loading && <CircularProgress />}

      {feedback && (
        <Paper elevation={3} style={{ padding: 20, marginTop: 20, maxWidth: 600 }}>
          <Typography variant="h6">Analysis:</Typography>
          <Typography style={{ whiteSpace: "pre-line" }}>{feedback}</Typography>
        </Paper>
      )}
    </Box>
  );
};

export default ResumeUpload;
