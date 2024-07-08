import { api } from "@/lib/axios"

type postFileParams = {
  file: File
}

const postFile = async (body: postFileParams) => {
  const formData = new FormData();
  formData.append('file', body.file); 
  return await api.post('v1/file/', formData, {
    headers: { 'Content-Type': 'multipart/form-data' },
  });
  // return await api.post('v1/file/upload/', body)
}

export { postFile }
