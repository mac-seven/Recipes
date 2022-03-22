from autopkglib import Processor, ProcessorError

__all__ = ["SampleSharedProcessor"]


class SampleSharedProcessor(Processor):
    """This processor doesn't do anything useful. It is a demonstration of using
    a shared processor via a recipe repo."""

    description = __doc__
    input_variables = {
        "shared_processor_input_var": {
            "required": True,
            "description": "Test the use of an input variable in a shared processor.",
        }
    }
    output_variables = {
        "module_file_path": {"description": "Outputs this module's file path."}
    }

    def main(self):
        // do stuff here
        print("My custom processor!")


if __name__ == "__main__":
    PROCESSOR = SampleSharedProcessor()
    PROCESSOR.execute_shell()
