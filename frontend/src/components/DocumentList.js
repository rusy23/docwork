import React, { useState, useEffect } from 'react';
import axios from 'axios';

const DocumentList = () => {
    const [documents, setDocuments] = useState([]);

    useEffect(() => {
        axios.get("http://localhost:8000/documents/")
            .then(response => {
                setDocuments(response.data);
            });
    }, []);

    const getStatusColor = (statusColor) => {
        if (statusColor === "red") {
            return { color: 'red' };
        } else if (statusColor === "yellow") {
            return { color: 'yellow' };
        } else if (statusColor === "green") {
            return { color: 'green' };
        }
    }

    return (
        <div>
            <h2>Document List</h2>
            <ul>
                {documents.map(doc => (
                    <li key={doc.id} style={getStatusColor(doc.status_color)}>
                        {doc.title} - {doc.date_received} - {doc.due_date}
                    </li>
                ))}
            </ul>
        </div>
    );
}

export default DocumentList;
