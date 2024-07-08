import { api } from "@/lib/axios"

const getHistory = async () => {
  return await api.get('/v1/file/history')
}

export { getHistory }
