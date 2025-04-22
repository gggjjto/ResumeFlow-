import React, { useState } from 'react';

interface FormData {
    name: string;
    email: string;
    phone: string;
    education: string;
    experience: string;
    skills: string;
}

const ResumeForm: React.FC<{ onSubmit: (data: FormData) => void }> = ({ onSubmit }) => {
    const [formData, setFormData] = useState({
        name: '',
        email: '',
        phone: '',
        education: '',
        experience: '',
        skills: '',
    });

    const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>) => {
        const { name, value } = e.target;
        setFormData({ ...formData, [name]: value });
    };

    const handleSubmit = (e: React.FormEvent) => {
        e.preventDefault();
        onSubmit(formData);
    };

    return (
        <form onSubmit={handleSubmit}>
            <div>
                <label>Name:</label>
                <input type="text" name="name" value={formData.name} onChange={handleChange} required />
            </div>
            <div>
                <label>Email:</label>
                <input type="email" name="email" value={formData.email} onChange={handleChange} required />
            </div>
            <div>
                <label>Phone:</label>
                <input type="tel" name="phone" value={formData.phone} onChange={handleChange} required />
            </div>
            <div>
                <label>Education:</label>
                <textarea name="education" value={formData.education} onChange={handleChange} required />
            </div>
            <div>
                <label>Experience:</label>
                <textarea name="experience" value={formData.experience} onChange={handleChange} required />
            </div>
            <div>
                <label>Skills:</label>
                <textarea name="skills" value={formData.skills} onChange={handleChange} required />
            </div>
            <button type="submit">Generate Resume</button>
        </form>
    );
};

export default ResumeForm;