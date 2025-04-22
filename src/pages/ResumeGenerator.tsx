import React, { useState } from 'react';
import ResumeForm from '../components/ResumeForm';
import ResumePreview from '../components/ResumePreview';

const ResumeGenerator: React.FC = () => {
    const [resumeData, setResumeData] = useState({
        name: '',
        email: '',
        phone: '',
        education: '',
        experience: '',
        skills: '',
    });

    const handleFormSubmit = (data: typeof resumeData) => {
        setResumeData(data);
    };

    return (
        <div className="resume-generator">
            <h1>简历生成器</h1>
            <ResumeForm onSubmit={handleFormSubmit} />
            <ResumePreview data={resumeData} />
        </div>
    );
};

export default ResumeGenerator;