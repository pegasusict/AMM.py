class UI:
    """
    :version:0.0.0
    :author:Mattijs Snepvangers
    """

    def action(self, action: str, **kwargs):
        """


        @return  :
        @author
        """
        pass

    def menu(self):
        """


        @return  :
        @author
        """
        pass

    def view(self):
        """


        @return  :
        @author
        """
        pass

    #
    # def progress(workers)
    #   from multiprocessing import Pool
    #   from tqdm.auto import tqdm
    #   with Pool(workers) as pool:
    #     results = list(tqdm(pool.imap(worker, thread_list, total=len(thread_list))

    def __call__(self, *args, **kwargs):
        viable_commands = ("delete", "edit", "import",)
