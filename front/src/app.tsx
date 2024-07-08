import * as Components from "@/components";
import { FileActionType, useFileContext } from "@/components/ui/file";
import { FileProcessingHistory } from "@/components/file-processing-history";
import { postFile } from "@/api/post-file";
import { getHistory } from "@/api/get-history";
import { useToast } from "@/components/ui/use-toast";
import axios from "axios";

const App = () => {
  const { state, dispatch } = useFileContext();
  const { toast } = useToast();

  const inputFileHandler = (file: File | undefined) => {
    dispatch({ type: FileActionType.ADD, payload: { file } });
  };

  const uploadFileHandler = async () => {
    if (!state.file) return;

    let newFileHistory = state.fileHistory;

    try {
      dispatch({
        type: FileActionType.ADD,
        payload: {
          isSubmitting: true,
        },
      });

      await postFile({ file: state.file });
      const responseHistory = await getHistory();

      newFileHistory = responseHistory.data

    } catch (err) {
      if (axios.isAxiosError(err) && err.response?.data) {
        newFileHistory.push(err.response.data);
      }

      toast({
        description: "Erro ao enviar arquivo",
        variant: "destructive",
      });
    } finally {
      dispatch({
        type: FileActionType.ADD,
        payload: {
          isSubmitting: false,
          fileHistory: newFileHistory,
        },
      });
    }
  };

  return (
    <Components.Layout>
      <Components.FileUploader
        file={state.file}
        onFileChange={inputFileHandler}
        onUpload={uploadFileHandler}
      />
      <FileProcessingHistory />
    </Components.Layout>
  );
};

export { App };
