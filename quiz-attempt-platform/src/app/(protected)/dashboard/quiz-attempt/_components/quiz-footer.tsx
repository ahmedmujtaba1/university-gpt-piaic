import { Button } from "@/components/ui/button";

interface QuizFooterProps {
  timeStart: string;
  totalPoints: number;
  onFinish: () => Promise<void>;
  onNext: () => void;
  isLastQuestion: boolean;
}

export const QuizAttemptFooter: React.FC<QuizFooterProps> = ({ timeStart, totalPoints, onFinish, onNext, isLastQuestion }) => (
  <div className="mt-8 flex items-center justify-between">
    <div className="flex items-center space-x-2 text-gray-500 dark:text-gray-400">
      <span>Time Start: {timeStart}</span>
      <span>•</span>
      <span>Total Points: {totalPoints}</span>
    </div>
    <div className="flex space-x-4">
      {isLastQuestion && (
        <Button onClick={onFinish} variant="outline">
          Finish
        </Button>
      )}
      {!isLastQuestion && <Button onClick={onNext}>Save & Next</Button>}
    </div>
  </div>
);
