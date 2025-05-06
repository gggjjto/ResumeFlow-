import axios from 'axios';
import type { ResumeForm } from '../types/resume';

const openaiApi = axios.create({
  baseURL: 'https://api.openai.com/v1',
  headers: {
    'Content-Type': 'application/json',
    'Authorization': `Bearer ${import.meta.env.VITE_OPENAI_API_KEY}`
  }
});

export async function generateResumeContent(resumeData: ResumeForm) {
  const prompt = `
    请基于以下信息生成一份专业的简历内容：
    姓名：${resumeData.basicInfo.name}
    职位：${resumeData.basicInfo.title}
    教育背景：${JSON.stringify(resumeData.education)}
    工作经验：${JSON.stringify(resumeData.experience)}
    技能：${resumeData.skills.join(', ')}
    
    请生成一份专业、简洁的简历内容，突出关键成就和技能。
  `;

  try {
    const response = await openaiApi.post('/chat/completions', {
      model: "gpt-3.5-turbo",
      messages: [
        {
          role: "system",
          content: "你是一位专业的HR助手，擅长优化简历内容。"
        },
        {
          role: "user",
          content: prompt
        }
      ],
      temperature: 0.7,
    });

    return response.data.choices[0].message.content;
  } catch (error) {
    console.error('AI生成简历失败:', error);
    throw error;
  }
}
