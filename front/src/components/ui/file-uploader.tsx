import { useFileContext } from "./file";

type FileUploaderProps = {
  file: File | null;
  onFileChange: (file: File | undefined) => void;
  onUpload: () => void;
}

const FileUploader = ({ file, onFileChange, onUpload }: FileUploaderProps) => {
  const { state: { isSubmitting } } = useFileContext();
  return (
    <div className = "flex flex-col gap-6">
      <div>
        <label htmlFor="file" className="sr-only">
          Choose a file
        </label>
        <input id="file" type="file"
              accept="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet,application/vnd.ms-excel,text/csv"
              onChange={(event) => onFileChange(event.target.files?.[0])}  />
      </div>
      {file && (
        <section>
          <p className="pb-6">File details:</p>
          <ul>
            <li>Name: {file.name}</li>
            <li>Type: {file.type}</li>
            <li>Size: {file.size} bytes</li>
          </ul>
        </section>
      )}

      {file && <button disabled={isSubmitting} className="rounded-lg bg-green-800 text-white px-4 py-2 border-none font-semibold disabled:opacity-70" onClick={() => onUpload()}>Upload the file</button>}
    </div>
  );
};

export { FileUploader };
