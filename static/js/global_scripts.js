        setTimeout(() => {
            const messages = document.querySelectorAll('[class*="animate-slide-down"]');
            messages.forEach(msg => {
                msg.style.transition = 'opacity 0.5s';
                msg.style.opacity = '0';
                setTimeout(() => msg.remove(), 500);
            });
        }, 5000);

        function openModal(modalId) {
            const modal = document.getElementById(modalId);
            if (modal) {
                modal.classList.remove('hidden');
                document.body.style.overflow = 'hidden';
            }
        }

        function closeModal(modalId) {
            const modal = document.getElementById(modalId);
            if (modal) {
                modal.classList.add('hidden');
                document.body.style.overflow = 'auto';
            }
        }

        document.addEventListener('click', function(e) {
            if (e.target.classList.contains('modal-backdrop')) {
                e.target.closest('.modal-container').classList.add('hidden');
                document.body.style.overflow = 'auto';
            }
        });

        document.addEventListener('keydown', function(e) {
            if (e.key === 'Escape') {
                const modals = document.querySelectorAll('.modal-container:not(.hidden)');
                modals.forEach(modal => {
                    modal.classList.add('hidden');
                    document.body.style.overflow = 'auto';
                });
            }
        });