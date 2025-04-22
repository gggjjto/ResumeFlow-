export const formatResumeData = (data: any) => {
    return {
        name: data.name || '',
        email: data.email || '',
        phone: data.phone || '',
        education: data.education || [],
        experience: data.experience || [],
        skills: data.skills || [],
    };
};

export const validateEmail = (email: string) => {
    const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return re.test(String(email).toLowerCase());
};

export const generateUniqueId = () => {
    return 'id-' + Math.random().toString(36).substr(2, 16);
};