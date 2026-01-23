import { useState } from "react";

function App() {
  const [image, setImage] = useState(null);
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleUpload = async () => {
    if (!image) return;

    setLoading(true);
    const formData = new FormData();
    formData.append("image", image);

    const res = await fetch("http://127.0.0.1:8000/api/analyze-fridge", {
      method: "POST",
      body: formData
    });

    const data = await res.json();
    setResult(data);
    setLoading(false);
  };

  return (
    <div style={{ padding: 20, maxWidth: 600, margin: "auto" }}>
      <h2>🥗 AI Fridge Chef</h2>

      <input
        type="file"
        accept="image/*"
        capture="environment"
        onChange={(e) => setImage(e.target.files[0])}
      />

      <br /><br />

      <button onClick={handleUpload} disabled={loading}>
        {loading ? "Analyzing..." : "Analyze Fridge"}
      </button>

      {result && (
        <>
          <h3>🧺 Ingredients Detected</h3>
          <ul>
            {result.ingredients.map((i) => (
              <li key={i}>{i}</li>
            ))}
          </ul>

          <h3>🍳 Recipes (≤30 mins)</h3>
          {result.recipes.map((r, idx) => (
            <div key={idx} style={{ border: "1px solid #ccc", padding: 10, marginBottom: 10 }}>
              <strong>{r.dish}</strong>
              <p>⏱ {r.time_minutes} mins · {r.difficulty}</p>

              <p><b>Steps:</b></p>
              <ol>
                {r.quick_steps.map((s, i) => (
                  <li key={i}>{s}</li>
                ))}
              </ol>
            </div>
          ))}
        </>
      )}
    </div>
  );
}

export default App;
