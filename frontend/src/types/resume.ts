export interface BasicInfo {
  name: string;
  email: string;
  phone: string;
  title: string;
}

export interface Education {
  school: string;
  major: string;
  degree: string;
  graduationYear: string;
}

export interface Experience {
  company: string;
  position: string;
  startDate: string;
  endDate: string;
  description: string;
}

export interface ResumeForm {
  basicInfo: BasicInfo;
  education: Education[];
  experience: Experience[];
  skills: string[];
  aiContent?: string;
}