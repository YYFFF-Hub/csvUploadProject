import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [file, setFile] = useState(null);
  const [csvData, setCsvData] = useState([]);  // 用于存储CSV数据
  const [message, setMessage] = useState('');  // 用于显示消息

  const handleFileChange = (event) => {
    setFile(event.target.files[0]);
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    const formData = new FormData();
    formData.append('file', file);

    axios.post('http://127.0.0.1:5000/upload', formData, {
      headers: {
        'Content-Type': 'multipart/form-data'
      }
    })
    .then(response => {
      setMessage(response.data.message);
      setCsvData(response.data.csv_data);  // 保存CSV数据
    })
    .catch(error => {
      console.error('上传失败', error);
      setMessage('上传失败');
    });
  };

  return (
    <div className="App">
      <h1>CSV 文件上传</h1>
      <form onSubmit={handleSubmit}>
        <input type="file" onChange={handleFileChange} />
        <button type="submit">上传</button>
      </form>

      {/* 显示上传成功的消息 */}
      {message && <p>{message}</p>}

      {/* 显示 CSV 数据 */}
      {csvData.length > 0 && (
        <div>
          <h2>上传的 CSV 文件数据：</h2>
          <table border="1">
            <thead>
              <tr>
                {Object.keys(csvData[0]).map((key) => (
                  <th key={key}>{key}</th>
                ))}
              </tr>
            </thead>
            <tbody>
              {csvData.map((row, index) => (
                <tr key={index}>
                  {Object.values(row).map((value, i) => (
                    <td key={i}>{value}</td>
                  ))}
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
    </div>
  );
}

export default App;