import React from 'react';

interface ResumePreviewProps {
    data: {
        name: string;
        email: string;
        phone: string;
        education: string;
        experience: string;
        skills: string;
    };
}

const ResumePreview: React.FC<ResumePreviewProps> = ({ data }) => {
    return (
        <div className="resume-preview">
            <h2>Preview</h2>
            <p>Name: {data.name}</p>
            <p>Email: {data.email}</p>
            <p>Phone: {data.phone}</p>
            <p>Education: {data.education}</p>
            <p>Experience: {data.experience}</p>
            <p>Skills: {data.skills}</p>
        </div>
    );
};

export default ResumePreview;