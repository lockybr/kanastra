import { useEffect } from "react";
import * as Components from "./ui";
import { FileActionType, useFileContext } from "./ui/file";
import { getHistory } from "@/api/get-history";
import { useToast } from "./ui/use-toast";

export type HistoryDetails = {
  timestamp: string;
  filename: string;
  size: string;
  amount_registers: string;
};

const FileProcessingHistory = () => {
  const {
    state: { isLoading, fileHistory },
    dispatch,
  } = useFileContext();
  const { toast } = useToast()

  useEffect(() => {
    const getFilesHistory = async () => {
      let history = []

      try {
        dispatch({
          type: FileActionType.ADD,
          payload: {
            isLoading: true,
          },
        });

        const response = await getHistory();

        history = response.data
      } catch (ex) {
        toast({
          description: 'Erro ao buscar histórico de processamento',
          variant: 'destructive'
        })
      } finally {
        dispatch({
          type: FileActionType.ADD,
          payload: {
            isLoading: false,
            fileHistory: history,
          },
        });
      }
    };

    getFilesHistory();
  }, []);

  if (isLoading) {
    return (
      <Components.Skeleton className="w-full h-full" />
    );
  }

  if (fileHistory.length === 0) {
    return (
      <div className="w-full h-full flex items-center justify-center">
        <p>Sem histórico de processamento</p>
      </div>
    );
  }

  return (
    <Components.ScrollArea className="flex-1">
      <Components.Table>
        <Components.TableHeader>
          <Components.TableRow>
            <Components.TableHead>Data e Hora</Components.TableHead>
            <Components.TableHead>Nome do Arquivo</Components.TableHead>
            <Components.TableHead>
              Tamanho do arquivo (em bytes)
            </Components.TableHead>
            <Components.TableHead>Qtd. Registros</Components.TableHead>
          </Components.TableRow>
        </Components.TableHeader>
        <Components.TableBody>
          {
            fileHistory.map((item) => {
            return (
              <Components.TableRow key={item.timestamp}>
                <Components.TableCell>{item.timestamp}</Components.TableCell>
                <Components.TableCell>{item.filename}</Components.TableCell>
                <Components.TableCell>{item.size}</Components.TableCell>
                <Components.TableCell>{item.amount_registers}</Components.TableCell>
              </Components.TableRow>
            );
          })}
        </Components.TableBody>
      </Components.Table>
    </Components.ScrollArea>
  );
};

export { FileProcessingHistory };
